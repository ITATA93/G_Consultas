# Tools_DataMover_Process.TrakResolvePatientCTReferences_MessagesSent

**Schema:** Tools_DataMover_Process
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TrakResolvePatientCTReferences | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| MessagesSent | varchar |  |  | SI | MessagesSent |
| element_key | varchar |  |  | NO | %MessagesSent array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*