from odoo import api, fields, models


class obat(models.Model):
    _name = 'obat.apotek'
    _description = 'New Description'

    id_obat = fields.Integer(string='Id')
    pembuat_obat = fields.Char(string='Pembuat')
    stok_obat = fields.Integer(string='Stok')

    comment_stok = fields.Char(compute='_compute_stok', string='Keterangan Stok')
    
    @api.depends('stok_obat')
    def _compute_stok(self):
        for record in self:
            if record.stok_obat < 50:
                record.stok = 'Ketersediaan Hampir Habis'
            else :
                record.stok = 'Ketersediaan Aman'