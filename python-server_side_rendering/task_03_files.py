from flask import Flask, render_template
import json
from flask import request
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    # Ouvre le fichier JSON contenant les données (liste d'objets)
    with open("items.json", "r") as file:
        data = json.load(file)  # Charge le contenu JSON dans une var. Python
        # Récupère la liste associée à la clé "items",
        # ou une liste vide si elle est absente
        items = data.get("items", [])
    # Return le template items.html en lui passant la liste d'objets récupérée
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    # Récupère les paramètres dans l'URL : source (obligatoire), id (optionnel)
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Chargement des données selon la source demandée
    if source == "json":
        with open("products.json") as file:
            data = json.load(file)

    elif source == "csv":
        with open("products.csv") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    else:
        # Si la source est inconnue, afficher un message d'erreur
        return render_template('product_display.html',
                               error="wrong source")

    # Si aucun id n'est donné, afficher tous les produits
    if product_id is None:
        return render_template("product_display.html", products=data)

    # Sinon, filtrer par id (casté en entier)
    product_id = int(product_id)
    product = None

    for p in data:
        print(">>", p)
        # Vérif. que le champ "id" existe dans l'élément avant de le comparer
        if "id" in p and int(p["id"].strip()) == product_id:
            product = p
            break

    # Si aucun produit trouvé avec cet id, afficher une erreur
    if product is None:
        return render_template("product_display.html",
                               error="Product not found")

    # Sinon, afficher le produit sous forme de liste
    # (pour compatibilité avec le template)
    return render_template("product_display.html", products=[product])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
