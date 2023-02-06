from selene.support.shared import browser

def delete_interrupt_elements():

    '''
    For delete google adds
    '''

    browser.execute_script('document.querySelector(".Advertisement-Section").remove')


def resource(path):
    import practice
    from pathlib import Path
    return str(
        Path(practice.__file__)
        .parent
        .parent
        .joinpath(f'practice/resources/{path}')
    )

