# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from openerp.osv import fields, osv

class res_helpdesk(osv.osv):    
	_name = 'res.helpdesk'		   
	_columns = {
		'name':fields.char('No. Ticket', readonly=True),
		'departamento':fields.char('Departamento', size=20,required=True),       
		'puesto':fields.char('Puesto', required=True),
		'descripcion':fields.text('Descripcion problema', required=True),
		'descripcion_resol':fields.text('Descripcion resolucion', 
				read=['helpdesk.all_users','helpdesk.helpdesk','base.group_system'],
				write=['helpdesk.helpdesk','base.group_system']),
		'usuario': fields.many2one(
				'res.users',
				'Usuario', readonly=True),
		'usuario_sol': fields.many2one(
				'res.users',
				'Solucionado por: ', 
				read=['helpdesk.all_users','helpdesk.helpdesk','base.group_system'],
				write=['helpdesk.helpdesk','base.group_system']),
		'fecha':fields.date('Fecha', required=True),
		'fecha_resol': fields.date('Fecha Resolución', 
				read=['helpdesk.all_users','helpdesk.helpdesk','base.group_system'],
				write=['helpdesk.helpdesk','base.group_system']),
		'estado':fields.selection((('a','Abierto'), ('c','Cerrado')),('Estado'), required=True)
	}
	  
	_defaults = {
		'estado' : 'a',
		'usuario': lambda obj, cr, uid, context: uid,
		'fecha': fields.date.today(),
		'name':lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'res.helpdesk.ticket'),
	}	
		
	def onchange_estado(self, cr, uid, ids, context=None):
		vals = {
			'usuario_sol': uid,
			'fecha_resol': fields.date.today(),
		}
		return {'value': vals}
		
res_helpdesk()
