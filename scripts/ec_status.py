#!/usr/bin/env python3
"""
ec2_status.py — Lista todas las instancias EC2 y su estado
"""
import boto3
from datetime import datetime

def listar_instancias():
    ec2 = boto3.client('ec2', region_name='sa-east-1')
    response = ec2.describe_instances()
    
    print("=" * 60)
    print(f"  ESTADO DE INSTANCIAS EC2 — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            instance_type = instance['InstanceType']
            
            # Obtener nombre del tag
            name = 'Sin nombre'
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name = tag['Value']
            
            # IP pública si está corriendo
            public_ip = instance.get('PublicIpAddress', 'Sin IP pública')
            
            # Emoji según estado
            emoji = '✅' if state == 'running' else '⛔' if state == 'stopped' else '🔄'
            
            print(f"\n{emoji} {name}")
            print(f"   ID:     {instance_id}")
            print(f"   Tipo:   {instance_type}")
            print(f"   Estado: {state}")
            print(f"   IP:     {public_ip}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    listar_instancias()
