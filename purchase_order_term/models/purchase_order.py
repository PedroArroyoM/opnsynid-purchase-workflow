# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    term_ids = fields.Many2many(
        string="Term(s)",
        comodel_name="purchase.term",
        column1="po_id",
        column2="term_id",
    )
