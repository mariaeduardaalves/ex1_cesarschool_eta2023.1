import unittest
from src.service.service_user import ServiceUser
from src.models.user import User


class TestServiceUser(unittest.TestCase):

    # Testes para o método add_user
    def test_add_user_valid(self):
        # Setup
        service = ServiceUser()

        # Chamada
        result = service.add_user("Alice", "Developer")

        # Avaliação
        self.assertEqual(result, "Usuário Adicionado com sucesso!")
        self.assertEqual(len(service.store.bd), 1)
        self.assertEqual(service.store.bd[0].name, "Alice")

    def test_add_user_existing(self):
        # Setup
        service = ServiceUser()
        service.add_user("Alice", "Developer")

        # Chamada
        result = service.add_user("Alice", "Developer")

        # Avaliação
        self.assertEqual(result, "Erro: Usuário com nome 'Alice' já existe!")

    def test_add_user_invalid_params(self):
        # Setup
        service = ServiceUser()

        # Chamada e Avaliação para None
        result = service.add_user(None, "QA")
        self.assertEqual(result, "Erro: 'name' e 'job' não podem ser nulos.")

        # Chamada e Avaliação para tipos errados
        result = service.add_user("Bob", 123)
        self.assertEqual(result, "Erro: 'name' e 'job' devem ser strings.")

    # Testes para o método remove_user
    def test_remove_user_existing(self):
        # Setup
        service = ServiceUser()
        service.add_user("Alice", "Developer")

        # Chamada
        result = service.remove_user("Alice")

        # Avaliação
        self.assertEqual(result, "Usuário 'Alice' removido com sucesso!")
        self.assertEqual(len(service.store.bd), 0)

    def test_remove_user_nonexistent(self):
        # Setup
        service = ServiceUser()

        # Chamada
        result = service.remove_user("Bob")

        # Avaliação
        self.assertEqual(result, "Erro: Usuário com nome 'Bob' não encontrado.")

    def test_remove_user_invalid_params(self):
        # Setup
        service = ServiceUser()

        # Chamada e Avaliação para None
        result = service.remove_user(None)
        self.assertEqual(result, "Erro: 'name' não pode ser nulo.")

        # Chamada e Avaliação para tipos errados
        result = service.remove_user(123)
        self.assertEqual(result, "Erro: 'name' deve ser uma string.")

    # Testes para o método update_user
    def test_update_user_existing(self):
        # Setup
        service = ServiceUser()
        service.add_user("Alice", "Developer")

        # Chamada
        result = service.update_user("Alice", "Senior Developer")

        # Avaliação
        self.assertEqual(result, "Trabalho do usuário 'Alice' atualizado para 'Senior Developer'.")
        self.assertEqual(service.store.bd[0].job, "Senior Developer")

    def test_update_user_nonexistent(self):
        # Setup
        service = ServiceUser()

        # Chamada
        result = service.update_user("Bob", "Manager")

        # Avaliação
        self.assertEqual(result, "Erro: Usuário com nome 'Bob' não encontrado.")

    def test_update_user_invalid_params(self):
        # Setup
        service = ServiceUser()

        # Chamada e Avaliação para None
        result = service.update_user(None, "Manager")
        self.assertEqual(result, "Erro: 'name' e 'new_job' não podem ser nulos.")

        result = service.update_user("Alice", None)
        self.assertEqual(result, "Erro: 'name' e 'new_job' não podem ser nulos.")

        # Chamada e Avaliação para tipos errados
        result = service.update_user(123, "Manager")
        self.assertEqual(result, "Erro: 'name' e 'new_job' devem ser strings.")

    # Testes para o método get_user_by_name
    def test_get_user_by_name_existing(self):
        # Setup
        service = ServiceUser()
        service.add_user("Alice", "Developer")

        # Chamada
        user = service.get_user_by_name("Alice")

        # Avaliação
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.job, "Developer")

    def test_get_user_by_name_nonexistent(self):
        # Setup
        service = ServiceUser()
        service.add_user("Alice", "Developer")

        # Chamada
        result = service.get_user_by_name("Bob")

        # Avaliação
        self.assertEqual(result, "Erro: Usuário com nome 'Bob' não encontrado.")

    def test_get_user_by_name_invalid_params(self):
        # Setup
        service = ServiceUser()

        # Chamada e Avaliação para None
        result = service.get_user_by_name(None)
        self.assertEqual(result, "Erro: 'name' não pode ser nulo.")

        # Chamada e Avaliação para tipos errados
        result = service.get_user_by_name(123)
        self.assertEqual(result, "Erro: 'name' deve ser uma string.")
