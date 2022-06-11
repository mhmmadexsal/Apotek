from odoo import api, fields, models


class transaksi(models.Model):
    _name = 'transaksi.apotek'
    _description = 'New Description'

    id_transaksi = fields.Integer(string='Id Transaksi')
    id_pasien = fields.One2many(comodel_name='pasien.apotek', inverse_name='id_pasien', string='Id Pasien')
    id_obat = fields.Many2one(comodel_name='obat_apotek', string='Obat')
    jml_transaksi = fields.Integer(string='Jumlah Transaksi')