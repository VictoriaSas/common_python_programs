import os
import yaml


def create_starter(starter):
    for folder, folders_filling in starter.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_tmp in folders_filling:
            if isinstance(data_tmp, dict):
                create_starter(data_tmp)
            else:
                if not os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')


pattern = {'my_project':
    [{'settings': [
        '__init__.py', 'dev.py', 'prod.py'
    ],
    },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py', {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]},
        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
            'authapp': ['base.html', 'index.html']}]
        }
                     ]
         }
    ]
}

with open('config.yaml', 'w') as f:
    f.write(yaml.dump(pattern))


with open("config.yaml") as y_file:
    starter_structure = yaml.safe_load(y_file)

path = input('Введите путь, в котором создать стартер: ')
# path = r'E:\resume\it_resume\Проекты\Программы питон (на гите)\common_python_programs'
os.chdir(path)
create_starter(starter_structure)
print('ready')

