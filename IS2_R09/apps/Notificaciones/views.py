# -*- encoding: utf-8 -*-

"""
    Modulo que contiene las distintas funciones necesarias para
    realizar las notificaciones correspondientes.  
    @author: Samuel Ruiz.
"""

from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def notificar(usuarios,subj,mensaje):
    """
        notificar(usuarios,subj,mensaje)
        Notificar
        =========
        
        Función encargada de realizar las notificaciones a los usuarios mediante el envió de mensajes
        a los correos electrónicos de cada uno de los afectados.
        @param usuarios: lista de usuarios al que se le notificará algún cambio.
        @param subj: Subjeto del mensaje.
        @param mensaje: Mensaje explicativo. 
    """
    try:
        for u in usuarios:
            mail= u.email
            send_mail(subj, mensaje, 'is2.pagiles@gmail.com',[mail], fail_silently=False)
    except:
        try:
            mail= usuarios.email
            send_mail(subj, mensaje, 'is2.pagiles@gmail.com',[mail], fail_silently=False)
        except:
            try:
                mail=usuarios
                send_mail(subj, mensaje, 'is2.pagiles@gmail.com',[mail], fail_silently=False)
            except:
                pass
        
def notificar_creacion_usuario(usuario):
    """
        notificar_creacion_usuario(usuario)
        Notificar Creación
        ==================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique la creación de un Usuario dentro del sistema.
        @param usuario: Usuario creado al que se notificará.
         
    """
    
    mensaje = u'Se ha creado su usuario éxitosamente.Su username es %s ' %(usuario.username)
    subj = u'Creación de cuenta IS2R09'
    notificar(usuario,subj,mensaje)
    
def notificar_mod_usuario(usuario):
    """
        notificar_mod_usuario(usuario)
        Notificar modificación
        ======================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique la modificación de un Usuario dentro del sistema.
        @param usuario: Usuario al que se notificará.
         
    """
    mensaje = u'Se han modificado uno o más campos de su cuenta. Por favor consulte la proxima vez que inicie sesión'
    subj = u'Modificacón de cuenta IS2R09'
    notificar(usuario,subj,mensaje)


def notificar_elim_usuario(usuario):
    """
        notificar_elim_usuario(usuario)
        Notificar Eliminación
        =====================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique la eliminación de un Usuario dentro del sistema.
        @param usuario: Usuario al que se notificará.
         
    """
    mensaje = u'Se ha eliminado su cuenta. Consulte con el administrador'
    subj = u'Eliminación de cuenta IS2R09'
    notificar(usuario,subj,mensaje)
    
def notificar_asignacion_proyecto(usuarios,proyecto):
    """
        notificar_asignacion_proyecto(usuarios,proyecto)
        Notificar Asignación
        ====================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique a uno o varios usuarios la asignación al equipo de un Proyecto.
        @param usuarios: Lista de usuarios asignados al Proyecto.
        @param proyecto: Proyecto al que se le asignó un equipo.
         
    """
    mensaje = u'Se le ha agregado al equipo del sgte Proyecto %s.Consulte la próxima vez que acceda al sistema ' %(proyecto)
    subj = u'Asignación Proyecto IS2R09'
    notificar(usuarios,subj,mensaje)
    

def notificar_mod_proyecto(usuarios,proyecto):
    """
        notificar_mod_proyecto(usuarios,proyecto)
        Notificar Modificación
        ======================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique al equipo de un Proyecto la modificación del mismo.
        @param usuarios: Lista de usuarios asignados al Proyecto.
        @param proyecto: Proyecto que se modificó.
         
    """
    mensaje = u'Se han realizado cambios en los campos del sgte Proyecto %s que tiene asignado.Consulte la próxima vez que acceda al sistema ' %(proyecto)
    subj = u'Modificación Proyecto IS2R09'
    notificar(usuarios,subj,mensaje)
    
def notificar_eli_proyecto(usuarios,proyecto):
    """
        notificar_eli_proyecto(usuarios,proyecto)
        Notificar Eliminación
        =====================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique al equipo de un Proyecto la Eliminación del mismo.
        @param usuarios: Lista de usuarios asignados al Proyecto.
        @param proyecto: Proyecto eliminado.
         
    """
    
    mensaje = u'Se ha eliminado el sgte Proyecto %s que tenía asignado.Consulte al administrador ' %(proyecto)
    subj = u'Eliminación Proyecto IS2R09'
    notificar(usuarios,subj,mensaje)


def notificar_asignacion_us(usuarios,userst):
    """
        notificar_asignacion_us(usuarios,userst)
        Notificar Asignación
        ====================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique a uno o varios usuarios la asignación de un User Story.
        @param usuarios: Lista de usuarios asignados al User story.
        @param userst: User story al que se le asignó usuarios.
        @note: También notificará en el caso de que ocurran cambios en los campos del User Story.
         
    """
    mensaje = u'Se le ha asignado la realización del sgte User Story %s.Consulte la próxima vez que acceda al sistema ' %(userst)
    subj = u'Asignación User Story IS2R09'
    notificar(usuarios,subj,mensaje)
    
def notificar_eli_us(usuarios,userst):
    """
        notificar_eli_us(usuarios,userst)
        Notificar Eliminación
        =====================
        
        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique a uno o varios usuarios la eliminación de un User Story.
        @param usuarios: Lista de usuarios asignados al User story.
        @param userst: User story al que se le asignó usuarios.
         
    """
    mensaje = u'Se ha eliminado el sgte User Story %s que tenía asignado.Consulte al administrador ' %(userst)
    subj = u'Eliminación User Story IS2R09'
    notificar(usuarios,subj,mensaje)
