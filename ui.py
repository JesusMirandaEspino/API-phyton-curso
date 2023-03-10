import database as db
import helpers
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

class CenterWidgetMixin:
    def center(self,):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.geometry(f"{w}x{h}+{x}+{y}")


class CreateClientWIndow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title = "Crear Cliente"
        self.build()
        self.center()
        self.transient( parent )
        self.grab_set()
    
    def build(self):
        frame = Frame(self)
        frame.pack( padx=20, pady=10 )
        Label( frame, text='DNI (2 int and 1 upper chart)' ).grid(row=0, column=0)
        Label(frame, text='Nombre (2  to 30 chart)').grid(row=0, column=1)
        Label(frame, text='Apellido (2  to 30 chart)').grid(row=0, column=2)

        dni = Entry(frame)
        dni.grid(row=1, column=0)
        dni.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 2))


        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text="Crear", command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)

        cancelar = Button(frame, text="Cancelar", command=self.close)
        cancelar.grid(row=0, column=1)

        self.validaciones = [0, 0, 0]  # False, False, False
        self.crear = crear

        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido


    
    def create_client(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.dni.get(),
            values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()
        

    def validate(self, event, index):
        valor = event.widget.get()
        # Validar como dni si es el primer campo o textual para los otros dos
        valido = helpers.dni_valido(valor, db.Clientes.lista) if index == 0 \
            else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})

        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)


class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Actualizar cliente')
        self.build()
        self.center()
        # Obligar al usuario a interactuar con la subventana
        self.transient(parent)
        self.grab_set()

    def build(self):
        # Top frame
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Labels
        Label(frame, text="DNI (no editable)").grid(row=0, column=0)
        Label(frame, text="Nombre (2 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Apellido (2 a 30 chars)").grid(row=0, column=2)

        # Entries
        dni = Entry(frame)
        dni.grid(row=1, column=0)
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))

        # Set entries initial values
        cliente = self.master.treeview.focus()
        campos = self.master.treeview.item(cliente, 'values')
        dni.insert(0, campos[0])
        dni.config(state=DISABLED)
        nombre.insert(0, campos[1])
        apellido.insert(0, campos[2])

        # Bottom frame
        frame = Frame(self)
        frame.pack(pady=10)

        # Buttons
        actualizar = Button(frame, text="Actualizar",
                            command=self.update_client)
        actualizar.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        # Update button activation
        self.validaciones = [1, 1]  # True, True

        # Class exports
        self.actualizar = actualizar
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def validate(self, event, index):
        valor = event.widget.get()
        valido = (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        # Cambiar estado del botón en base a las validaciones
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)


    def update_client(self):
        cliente = self.master.treeview.focus()
        # Sobreescribimos los datos de la fila seleccionada
        self.master.treeview.item(
            cliente, values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.modificar(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()


    def close(self):
        self.destroy()
        self.update()


class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title('Gestor de Clientes')
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ( 'DNI','Nombre', 'Apellido' )

        treeview.column('#0', width=0, stretch=NO)
        treeview.column('DNI', anchor=CENTER)
        treeview.column('Nombre', anchor=CENTER)
        treeview.column('Apellido', anchor=CENTER)

        treeview.heading('DNI', text='DNI', anchor=CENTER)
        treeview.heading('Nombre', text='Nombre', anchor=CENTER)
        treeview.heading('Apellido', text='Apellido', anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack( side=RIGHT, fill=Y )
        treeview['yscrollcommand'] = scrollbar.set

        for cliente in db.Clientes.lista:
            treeview.insert( parent='', index='end', iid=cliente.dni, 
                            values=( cliente.dni, cliente.nombre, cliente.apellido ))
        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text='Crear', command=self.create).grid( row=0, column=0 )
        Button(frame, text='Modificar', command=self.edit).grid(row=0, column=1)
        Button(frame, text='Borrar', command=self.delete).grid(row=0, column=2)

        self.treeview = treeview

    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item( cliente, 'values' )
            confirmar = askokcancel( title='Confirmar Borrado', message=f"¿Borrar campos {campos[1]} {campos[2]}", icon=WARNING )

        if(confirmar):
            self.treeview.delete(cliente)
            db.Clientes.borrar(campos[0])

    def create(self):
        CreateClientWIndow(self)

    def edit(self):
        EditClientWindow(self)

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()