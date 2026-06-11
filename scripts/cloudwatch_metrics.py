#!/usr/bin/env python3
"""
cloudwatch_metrics.py — Lee métricas de CPU de EC2 desde CloudWatch
"""
import boto3
from datetime import datetime, timedelta, timezone

INSTANCE_ID = 'i-02d98a9ed249b0dbe'
REGION = 'sa-east-1'

def obtener_cpu():
    cw = boto3.client('cloudwatch', region_name=REGION)
    ahora = datetime.now(timezone.utc)
    hace_1h = ahora - timedelta(hours=1)
    
    print("=" * 60)
    print(f"  MÉTRICAS CLOUDWATCH — {ahora.strftime('%Y-%m-%d %H:%M')} UTC")
    print(f"  Instancia: {INSTANCE_ID}")
    print("=" * 60)
    
    response = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': INSTANCE_ID}],
        StartTime=hace_1h,
        EndTime=ahora,
        Period=300,
        Statistics=['Average', 'Maximum']
    )
    
    datapoints = sorted(response['Datapoints'], key=lambda x: x['Timestamp'])
    
    if not datapoints:
        print("\n  ⚠️  Sin datos — la instancia puede estar detenida")
        print("  Los datos aparecen cuando la instancia está running")
    else:
        print(f"\n  📊 CPU últimas 24 horas ({len(datapoints)} muestras):\n")
        for dp in datapoints[-5:]:
            tiempo = dp['Timestamp'].strftime('%H:%M')
            avg = dp['Average']
            maximo = dp['Maximum']
            barra = '█' * int(avg) + '░' * (100 - int(avg))
            print(f"  {tiempo} | Avg: {avg:.1f}% | Max: {maximo:.1f}%")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    obtener_cpu()
