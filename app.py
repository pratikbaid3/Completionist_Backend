from flask import Flask,request
from flask_restful import Resource, Api
import ps4_games

#BASE URL= https://completionist-api.herokuapp.com/

app=Flask(__name__, static_url_path='/public', static_folder='public/')
app.config['PROPAGATE_EXCEPTIONS']=True
app.secret_key='Pratik'
api=Api(app)

class PS4Games(Resource):
    def get(self):
        search=request.args.get('search','')
        page=request.args.get('page', 1)
        count=request.args.get('count', 50)
        try:
            game_list=ps4_games.get_games(page,count,search)
            if(game_list=='Error'):
                raise
            return {'result':{'games':game_list,'page':page,'count':count}},200
        except Exception as e:
            print('ERROR')
            return {'result':'Server Error'},500

class PS4Game(Resource):
    def get(self,name):
        try:
            game_list=ps4_games.get_game(name)
            if(game_list=='Error'):
                raise
            return {'result':{'games':game_list}},200
        except Exception as e:
            print('ERROR',e)
            return {'result':'Server Error'},500

class PS4GameGuide(Resource):
    def get(self,name):
        try:
            game_list=ps4_games.get_game_guide(name)
            if(game_list=='Error'):
                raise
            return {'result':{'games':game_list}},200
        except Exception as e:
            print('ERROR',e)
            return {'result':'Server Error'},500

api.add_resource(PS4Games,'/ps4/games')
api.add_resource(PS4Game,'/ps4/game/<string:name>')
api.add_resource(PS4GameGuide,'/ps4/game/guide/<string:name>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)