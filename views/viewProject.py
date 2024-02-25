from flask import Blueprint, render_template, request
from models.modelProject import modelProject

main = Blueprint("datatable_bp", __name__)


@main.route('/allBanks')
def getBanks():
    banks = modelProject.get_dataBank()
    return render_template('/mantenimiento.html', banks=banks)


@main.route('/insert', methods=['POST', 'GET'])
def insertBank():
    if request.method == "POST":
        data = request.get_json()
        descripcion = data.get('bank', None)
        modelProject.insert_bank(descripcion)
    return "OK"


@main.route('/update', methods=['POST', 'GET'])
def updateBank():
    if request.method == "POST":
        data = request.get_json()
        idbco = data.get('idbco', None)
        descripcion = data.get('bank', None)
        modelProject.update_bank(idbco, descripcion)
    return "OK"


@main.route('/delete', methods=['POST', 'GET'])
def deleteBank():
    if request.method == "POST":
        data = request.get_json()
        idbco = data.get('idbco', None)
        modelProject.delete_bank(idbco)
    return "OK"
