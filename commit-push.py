import os
import git


#Pushしたいリポジトリに移動
repository = git.Repo()

#最新を取り込むため一旦Pull
o = repository.remotes.origin
o.pull()

#Commit(サブディレクトリ含めて全て)
repository.git.commit('.','-m','\"Commit Log\"')

#Push
origin = repository.remote(name='origin')
origin.push()