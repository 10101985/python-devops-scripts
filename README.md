# Python DevOps Scripts 🐍

Scripts de automatización DevOps con Python y boto3 (AWS SDK).
Gestión de EC2, S3 y métricas CloudWatch desde la terminal.

## Scripts incluidos

### 🖥️ ec2_status.py
Lista todas las instancias EC2 con su estado, tipo, nombre e IP pública.

### 📦 s3_manager.py
Gestiona bucket S3: lista objetos, sube y descarga archivos con manejo de errores.

### 📊 cloudwatch_metrics.py
Lee métricas de CPU de instancias EC2 desde CloudWatch con visualización en terminal.

## Uso

```bash
python3 scripts/ec2_status.py
python3 scripts/s3_manager.py
python3 scripts/cloudwatch_metrics.py
```

## Requisitos

```bash
pip3 install boto3 --break-system-packages
```

AWS CLI configurado con credenciales válidas:
```bash
aws configure
```

## Conceptos aplicados

- **boto3** — SDK oficial de Python para AWS
- **Clientes boto3** — EC2, S3, CloudWatch
- **Manejo de errores** — try/except en operaciones AWS
- **Funciones Python** — código modular y reutilizable
- **datetime y timezone** — manejo de fechas UTC para métricas

## Tecnologías

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![boto3](https://img.shields.io/badge/boto3-FF9900?style=flat&logo=amazonaws&logoColor=white)

## Autor
Cristian Robledo Macleood — [LinkedIn](https://www.linkedin.com/in/cristian-robledo-macleood-7538331b5/) | [Portfolio](https://10101985.github.io/web-portfolio-personal)
