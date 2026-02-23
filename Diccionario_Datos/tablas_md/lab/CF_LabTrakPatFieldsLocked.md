# lab.CF_LabTrakPatFieldsLocked

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLPF_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFLPF_FieldsLocked | varchar |  |  | SI | Fields Locked |
| CFLPF_RowID | varchar |  |  | NO | - |
| CFLPF_UserGroup_DR | bigint |  | FK | NO | User Group |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*