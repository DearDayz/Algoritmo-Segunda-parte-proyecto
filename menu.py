from empresa import GestionEmpresas, Empresa
from proyecto import Proyecto
from datetime import datetime
import re

def mostrar_menu():
    try:
        print("Sistema de Gestión de Empresas y Proyectos")
        print("1. Crear empresa")
        print("2. Modificar empresa")
        print("3. Consultar empresa")
        print("4. Eliminar empresa")
        print("5. Listar empresas")
        print("6. Crear proyecto")
        print("7. Modificar proyecto")
        print("8. Consultar proyecto")
        print("9. Eliminar proyecto")
        print("10.Listar proyectos")
        print("0. Salir")
    except Exception as e:
        mostrar_menu()
        main()
def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False
def validar_id(id):
    return id.isdigit() and int(id) > 0
def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 11

def validar_correo(correo):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo) is not None
def validar_vacio(campo):
    return campo and campo.strip()
def solicitar_datos_empresa():
    try:
        id = input("ID: ")
        while not id.isdigit() or not id:
            print("El ID debe ser un número entero. Intente nuevamente.")
            id = input("ID: ")
        nombre = input("Nombre: ")
        while not validar_vacio(nombre) or not nombre.isalpha():
            print("nombre no puede estar vacío ni contener números. Intente nuevamente.")
            nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        while not validar_vacio(descripcion):
            print("Descripción no puede estar vacío. Intente nuevamente.")
            descripcion = input("Descripción: ")
        fecha_creacion = input("Fecha de creación (YYYY-MM-DD): ")
        while not validar_fecha(fecha_creacion):
            print("Fecha de creación inválida. Intente nuevamente.")
            fecha_creacion = input("Fecha de creación (YYYY-MM-DD): ")
        direccion = input("Dirección: ")
        while not validar_vacio(direccion):
            print("Dirección no puede estar vacío. Intente nuevamente.")
            direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        while not validar_telefono(telefono):
            print("Teléfono inválido. Intente nuevamente.")
            telefono = input("Teléfono: ")
        correo = input("Correo: ")
        while not validar_correo(correo):
            print("Correo inválido. Intente nuevamente.")
            correo = input("Correo: ")
        gerente = input("Gerente: ")
        while not validar_vacio(gerente):
            print("Gerente no puede estar vacío. Intente nuevamente.")
            gerente = input("Gerente: ")
        equipo_contacto = input("Equipo de contacto: ")
        while not validar_vacio(equipo_contacto):
            print("Equipo de contacto no puede estar vacío. Intente nuevamente.")
            equipo_contacto = input("Equipo de contacto: ")
        return Empresa(id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto)
    except Exception as e:
        mostrar_menu()
        main()
def solicitar_datos_proyecto():
    try:
        id = input("ID: ")
        while not id.isdigit() or not id:
            print("El ID debe ser un número entero. Intente nuevamente.")
            id = input("ID: ")
        nombre = input("Nombre: ")
        while not nombre or not nombre.strip() or not nombre.isalpha():
            print("Nombre no puede estar vacío ni contener números. Intente nuevamente.")
            nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        while not validar_vacio(descripcion):
            print("Descripción no puede estar vacío. Intente nuevamente.")
            descripcion = input("Descripción: ")
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        while not validar_fecha(fecha_inicio):
            print("Fecha de inicio inválida. Intente nuevamente.")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
        while not validar_fecha(fecha_vencimiento):
            print("Fecha de vencimiento inválida. Intente nuevamente.")
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
        estado_actual = input("Estado actual: ")
        while not validar_vacio(estado_actual):
            print("Estado actual no puede estar vacío. Intente nuevamente.")
            estado_actual = input("Estado actual: ")
        empresa = input("Empresa: ")
        while not validar_vacio(empresa):
            print("Empresa no puede estar vacío. Intente nuevamente.")
            empresa = input("Empresa: ")
        gerente = input("Gerente: ")
        while not validar_vacio(gerente):
            print("Gerente no puede estar vacío. Intente nuevamente.")
            gerente = input("Gerente: ")
        equipo = input("Equipo: ")
        while not validar_vacio(equipo):
            print("Equipo no puede estar vacío. Intente nuevamente.")
            equipo = input("Equipo: ")
        return Proyecto(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo)
    except Exception as e:
        mostrar_menu()
        main()

def main():
    try:
        gestion_empresas = GestionEmpresas('empresas.csv')

        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                empresa = solicitar_datos_empresa()
                gestion_empresas.crear_empresa(empresa)
            elif opcion == '2':
                id = input("Ingrese el ID de la empresa a modificar: ")
                nuevos_datos = {}
                print("Deje en blanco los campos que no desee modificar.")
                #validar inputs
                dato = input("Nuevo nombre: ")
                if dato:
                    while not dato.isalpha():
                        print("Nombre no válido. Intente nuevamente.")
                        dato = input("Nuevo nombre: ")
                nuevos_datos['nombre'] = dato

                nuevos_datos['descripcion'] = input("Nueva descripción: ")

                datos_fecha = input("Nueva fecha de creación (YYYY-MM-DD): ")
                if datos_fecha:
                    while not validar_fecha(datos_fecha):
                        print("Fecha de creación inválida. Intente nuevamente.")
                        datos_fecha = input("Nueva fecha de creación (YYYY-MM-DD): ")
                nuevos_datos['fecha_creacion'] = datos_fecha
                
                nuevos_datos['direccion'] = input("Nueva dirección: ")
                datos_telefono = input("Nuevo teléfono: ")
                if datos_telefono:
                    while not validar_telefono(datos_telefono):
                        print("Teléfono inválido. Intente nuevamente.")
                        datos_telefono = input("Nuevo teléfono: ")
                nuevos_datos['telefono'] = datos_telefono

                dato = input("Nuevo correo: ")
                if dato:
                    while not validar_correo(dato):
                        print("Correo inválido. Intente nuevamente.")
                        dato = input("Nuevo correo: ")
                nuevos_datos['correo'] = dato

                nuevos_datos['gerente'] = input("Nuevo gerente: ")
                nuevos_datos['equipo_contacto'] = input("Nuevo equipo de contacto: ")
                empresa = gestion_empresas.modificar_empresa(id, {k: v for k, v in nuevos_datos.items() if v})
                if empresa:
                    print("Empresa modificada con éxito.")
                else:
                    print("No se encontró la empresa.")
            elif opcion == '3':
                id = input("Ingrese el ID de la empresa a consultar: ")
                while not validar_id(id):
                    print("ID inválido. Intente nuevamente.")
                    id = input("Ingrese el ID de la empresa a consultar: ")
                empresa = gestion_empresas.consultar_empresa(id)
                if empresa:
                    print(empresa)
                else:
                    print("No se encontró la empresa.")
            elif opcion == '4':
                id = input("Ingrese el ID de la empresa a eliminar: ")
                while not validar_id(id):
                    print("ID inválido. Intente nuevamente.")
                    id = input("Ingrese el ID de la empresa a eliminar: ")
                gestion_empresas.eliminar_empresa(id)
                print("Empresa eliminada con éxito.")
            elif opcion == '5':
                for empresa in gestion_empresas.empresas:
                    print(empresa)
            elif opcion == '6':
                id_empresa = input("Ingrese el ID de la empresa para agregar un proyecto: ")
                while not validar_id(id_empresa):
                    print("ID inválido. Intente nuevamente.")
                    id_empresa = input("Ingrese el ID de la empresa para agregar un proyecto: ")
                empresa = gestion_empresas.consultar_empresa(id_empresa)
                if empresa:
                    proyecto = solicitar_datos_proyecto()
                    empresa.proyectos.insertar(proyecto)
                    gestion_empresas.guardar_empresas()
                    print("Proyecto creado con éxito.")
                else:
                    print("No se encontró la empresa.")
            elif opcion == '7':
                id_empresa = input("Ingrese el ID de la empresa para modificar un proyecto: ")
                while not validar_id(id_empresa):
                    print("ID inválido. Intente nuevamente.")
                    id_empresa = input("Ingrese el ID de la empresa para modificar un proyecto: ")
                empresa = gestion_empresas.consultar_empresa(id_empresa)
                if empresa:
                    id_proyecto = input("Ingrese el ID del proyecto a modificar: ")
                    while not validar_id(id_proyecto):
                        print("ID inválido. Intente nuevamente.")
                        id_proyecto = input("Ingrese el ID del proyecto a modificar: ")
                    proyecto = empresa.proyectos.consultar_proyecto(id_proyecto)
                    if proyecto:
                        nuevos_datos = {}
                        print("Deje en blanco los campos que no desee modificar.")
                        dato = input("Nuevo nombre: ")
                        if dato:
                            while not dato.isalpha():
                                print("Nombre no válido. Intente nuevamente.")
                                dato = input("Nuevo nombre: ")
                        nuevos_datos['nombre'] = dato
                        nuevos_datos['descripcion'] = input("Nueva descripción: ")
                        datos_fecha = input("Nueva fecha de inicio (YYYY-MM-DD): ")
                        if datos_fecha:
                            while not validar_fecha(datos_fecha):
                                print("Fecha de inicio inválida. Intente nuevamente.")
                                datos_fecha = input("Nueva fecha de inicio (YYYY-MM-DD): ")
                        nuevos_datos['fecha_inicio'] = datos_fecha
                        datos_fecha = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                        if datos_fecha:
                            while not validar_fecha(datos_fecha):
                                print("Fecha de vencimiento inválida. Intente nuevamente.")
                                datos_fecha = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                        nuevos_datos['fecha_vencimiento'] = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                        nuevos_datos['estado_actual'] = input("Nuevo estado actual: ")
                        nuevos_datos['empresa'] = input("Nueva empresa: ")
                        nuevos_datos['gerente'] = input("Nuevo gerente: ")
                        nuevos_datos['equipo'] = input("Nuevo equipo: ")
                        proyecto.nombre = nuevos_datos.get('nombre', proyecto.nombre)
                        proyecto.descripcion = nuevos_datos.get('descripcion', proyecto.descripcion)
                        proyecto.fecha_inicio = nuevos_datos.get('fecha_inicio', proyecto.fecha_inicio)
                        proyecto.fecha_vencimiento = nuevos_datos.get('fecha_vencimiento', proyecto.fecha_vencimiento)
                        proyecto.estado_actual = nuevos_datos.get('estado_actual', proyecto.estado_actual)
                        proyecto.empresa = nuevos_datos.get('empresa', proyecto.empresa)
                        proyecto.gerente = nuevos_datos.get('gerente', proyecto.gerente)
                        proyecto.equipo = nuevos_datos.get('equipo', proyecto.equipo)
                        gestion_empresas.guardar_empresas()
                        print("Proyecto modificado con éxito.")
                    else:
                        print("No se encontró el proyecto.")
                else:
                    print("No se encontró la empresa.")
            elif opcion == '8':
                id_empresa = input("Ingrese el ID de la empresa para consultar un proyecto: ")
                while not validar_id(id_empresa):
                    print("ID inválido. Intente nuevamente.")
                    id_empresa = input("Ingrese el ID de la empresa para consultar un proyecto: ")
                empresa = gestion_empresas.consultar_empresa(id_empresa)
                if empresa:
                    id_proyecto = input("Ingrese el ID del proyecto a consultar: ")
                    while not validar_id(id_proyecto):
                        print("ID inválido. Intente nuevamente.")
                        id_proyecto = input("Ingrese el ID del proyecto a consultar: ")
                    proyecto = empresa.proyectos.consultar_proyecto(id_proyecto)
                    if proyecto:
                        print(proyecto)
                    else:
                        print("No se encontró el proyecto.")
                else:
                    print("No se encontró la empresa.")
            elif opcion == '9':
                id_empresa = input("Ingrese el ID de la empresa para eliminar un proyecto: ")
                while not validar_id(id_empresa):
                    print("ID inválido. Intente nuevamente.")
                    id_empresa = input("Ingrese el ID de la empresa para eliminar un proyecto: ")
                empresa = gestion_empresas.consultar_empresa(id_empresa)
                if empresa:
                    id_proyecto = input("Ingrese el ID del proyecto a eliminar: ")
                    while not validar_id(id_proyecto):
                        print("ID inválido. Intente nuevamente.")
                        id_proyecto = input("Ingrese el ID del proyecto a eliminar: ")
                    proyecto = empresa.proyectos.consultar_proyecto(id_proyecto)
                    if proyecto:
                        empresa.proyectos.eliminar(proyecto)
                        gestion_empresas.guardar_empresas()
                        print("Proyecto eliminado con éxito.")
                    else:
                        print("No se encontró el proyecto.")
                else:
                    print("No se encontró la empresa.")
            elif opcion == '10':
                id_empresa = input("Ingrese el ID de la empresa para listar sus proyectos: ")
                while not validar_id(id_empresa):
                    print("ID inválido. Intente nuevamente.")
                    id_empresa = input("Ingrese el ID de la empresa para listar sus proyectos: ")
                empresa = gestion_empresas.consultar_empresa(id_empresa)
                if empresa:
                    for proyecto in empresa.proyectos.recorrido_in_orden(empresa.proyectos.raiz):
                        print(proyecto)
                else:
                    print("No se encontró la empresa.")
            elif opcion == '0':
                print("Saliendo del sistema.")
                break
            else:
                print("Opción no válida, intente nuevamente.")
    except Exception as e:
        mostrar_menu()
        main()

if __name__ == "__main__":
    main()
