# этот вариант - нерабоий!!!
import view
import model

def start():
    while True:
        input_edclass = view.select_class()
        main(input_edclass)

def main(educ_class: str):
    if educ_class == 'exit':
        view.exit_process()
    else:
        path = model.set_path(educ_class)
        jorn_list = model.call_jornal(path)
        view.show_journal(jorn_list)
        subj = view.select_subject()
        puple = view.who_answer()
        mark = view.what_mark()
        new_jorn_list = model.add_mark(jorn_list, subj, puple, mark)
        model.write_marks(new_jorn_list, path)
