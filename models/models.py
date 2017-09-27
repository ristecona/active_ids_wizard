# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api

class MergeIssuesLine(models.TransientModel):

    _name = 'base.product.catalog.line'
    _order = 'min_id asc'

    wizard_id = fields.Many2one('base.product.catalog.automatic.wizard', 'Wizard')
    min_id = fields.Integer('MinID')
    aggr_ids = fields.Char('Ids', required=True)

class EbMergeIssues(models.TransientModel):

    _name = 'base.product.catalog.automatic.wizard'
    _description = 'Assign catalog to products'

    @api.model
    def default_get(self, fields):
        res = super(EbMergeIssues, self).default_get(fields)
        active_ids = self.env.context.get('active_ids')
        if self.env.context.get('active_model') == 'product.template' and active_ids:
            res['product_ids'] = active_ids
        return res

    product_ids = fields.Many2many('product.template', string='Products')#'merge_issues_rel', 'merge_id', 'issue_id',)
    #user_id = fields.Many2one('res.users', 'Assigned to', index=True)
    #dst_issue_id = fields.Many2one('project.issue', string='Destination Issue')
    dst_catalog = fields.Many2one('catalog.pos.settings', string = "Catalog")

    @api.multi
    def action_merge_issues(self):
        for id in self.product_ids:
            _logger.info("ACTIVE ID: %s" %id.id)