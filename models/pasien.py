from odoo import api, fields, models
from datetime import date

class pasien(models.Model):
    _name = 'pasien.apotek'
    _description = 'New Description'

    id_pasien = fields.Many2one(comodel_name='transaksi_apotek', string='Id Pesien')
    nama_pasien = fields.Char(string='Nama Pasien')
    ttl_pasien = fields.Date(string='Tanggal Lahir Pasien')