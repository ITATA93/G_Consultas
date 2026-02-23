# lab.CF_LabtrakIP

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLIP_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFLIP_IP_Address | varchar |  |  | SI | IP Address |
| CFLIP_IntCode | varchar |  |  | NO | Interface Code |
| CFLIP_IntDesc | varchar |  |  | SI | Interface Description |
| CFLIP_MUMPS_Device | varchar |  |  | SI | MUMPS Device |
| CFLIP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*