#!/usr/bin/env python3
"""
s3_manager.py — Gestiona bucket S3: listar, subir y descargar archivos
"""
import boto3
import os
from datetime import datetime

BUCKET = 'cristian-devops-bucket-2026'
REGION = 'sa-east-1'

def listar_archivos():
    s3 = boto3.client('s3', region_name=REGION)
    print(f"\n📦 Contenido del bucket: {BUCKET}")
    print("-" * 50)
    try:
        response = s3.list_objects_v2(Bucket=BUCKET)
        objetos = response.get('Contents', [])
        if not objetos:
            print("  El bucket está vacío")
        for obj in objetos:
            size_kb = obj['Size'] / 1024
            fecha = obj['LastModified'].strftime('%Y-%m-%d %H:%M')
            print(f"  📄 {obj['Key']} — {size_kb:.1f} KB — {fecha}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

def subir_archivo(ruta_local, nombre_s3=None):
    s3 = boto3.client('s3', region_name=REGION)
    if not nombre_s3:
        nombre_s3 = os.path.basename(ruta_local)
    print(f"\n⬆️  Subiendo {ruta_local} → s3://{BUCKET}/{nombre_s3}")
    try:
        s3.upload_file(ruta_local, BUCKET, nombre_s3)
        print(f"  ✅ Subido exitosamente")
    except Exception as e:
        print(f"  ❌ Error: {e}")

def descargar_archivo(nombre_s3, ruta_local):
    s3 = boto3.client('s3', region_name=REGION)
    print(f"\n⬇️  Descargando s3://{BUCKET}/{nombre_s3} → {ruta_local}")
    try:
        s3.download_file(BUCKET, nombre_s3, ruta_local)
        print(f"  ✅ Descargado exitosamente")
    except Exception as e:
        print(f"  ❌ Error: {e}")

if __name__ == '__main__':
    print("=" * 50)
    print("  S3 MANAGER — Cristian Robledo Macleood")
    print("=" * 50)
    listar_archivos()
    subir_archivo('/home/macfly1985/monitor-sistema-bash/monitor.sh', 'backups/monitor.sh')
    listar_archivos()
