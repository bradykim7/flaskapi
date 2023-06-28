from flask import Blueprint, Flask, request, url_for, redirect

routes = Blueprint("crawl", __name__, url_prefix="/crawl")

@routes.route('/<string:website>' ,methods=['GET'])
def crawl_website(website):
    return "Crawling website: " + website
