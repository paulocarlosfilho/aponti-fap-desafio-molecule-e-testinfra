# 🛡️ DevSecOps: Automação e Validação de Infraestrutura Nginx com Molecule e Testinfra

Este repositório contém uma solução completa de **Infraestrutura como Código (IaC)** para o provisionamento e validação automatizada de um servidor web **Nginx** em ambiente Ubuntu 22.04.

O projeto utiliza a abordagem de **testes de infraestrutura modernos**, onde o ambiente de testes é provisionado de forma efêmera em contêineres Docker gerenciados pelo **Molecule**, e o estado real do sistema operacional é auditado via **Testinfra (Pytest)** antes da promoção para produção.

---

## 📐 Arquitetura da Solução

* **Ansible (IaC):** Automação declarativa para instalação e inicialização do serviço Nginx.
* **Molecule (Orquestrador):** Gerencia o ciclo de vida dos testes efêmeros (criação de contêineres Docker com `systemd`, teste de convergência, idempotência e destruição do ambiente).
* **Testinfra (Inspetor):** Suíte de testes em Python para auditoria do SO, garantindo que pacotes, serviços e portas de rede estejam em conformidade.
* **Docker:** Provedor de execução de ambientes isolados baseados em `geerlingguy/docker-ubuntu2204-ansible`.

---

## 📁 Estrutura do Projeto

```text
servidor_nginx/
├── meta/
│   └── main.yml              # Identificação e metadados da Role (FQRN: devsecops.servidor_nginx)
├── tasks/
│   └── main.yml              # Automação das tarefas (Instalação APT + Serviço Systemd)
└── molecule/
    └── default/
        ├── molecule.yml      # Plano diretor do Molecule (Docker + Systemd + Cgroups)
        ├── converge.yml      # Playbook de aplicação da role no contêiner
        └── tests/
            └── test_default.py # Script de testes em Python (Testinfra)