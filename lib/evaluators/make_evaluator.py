import imp
import os
from lib.datasets.dataset_catalog import DatasetCatalog


def _evaluator_factory(cfg):
    module = cfg.evaluator_module
    path = cfg.evaluator_path
    evaluator = imp.load_source(module, path).Evaluator()
    return evaluator #* 返回Evaluator类的实例，不需要参数


def make_evaluator(cfg):
    if cfg.skip_eval:
        return None
    else:
        return _evaluator_factory(cfg)
