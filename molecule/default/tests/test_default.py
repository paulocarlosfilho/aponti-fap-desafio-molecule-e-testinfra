import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nginx_pacote_instalado(host):
    """Valida se o pacote do Nginx foi instalado corretamente no SO."""
    pacote_nginx = host.package("nginx")
    assert pacote_nginx.is_installed


def test_nginx_servico_rodando_e_habilitado(host):
    """Valida se o servico do Nginx esta ativo e habilitado para iniciar no boot."""
    servico_nginx = host.service("nginx")
    assert servico_nginx.is_running
    assert servico_nginx.is_enabled


def test_nginx_porta_80_escutando(host):
    """Valida se o servidor Nginx esta escutando na porta 80 (HTTP)."""
    porta_web = host.socket("tcp://0.0.0.0:80")
    assert porta_web.is_listening