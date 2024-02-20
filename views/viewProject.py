from flask import Blueprint, render_template, request
from models.modelProject import modelProject

main = Blueprint("datatable_bp", __name__)


@main.route('/allBanks')
def getBanks():
    banks = modelProject.get_dataBank()
    return render_template('/mantenimiento.html', banks=banks)
