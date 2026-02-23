# SQLUser.PA_PathwayItemRole

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHIR_ParRef | varchar | PK |  | NO | Parent Reference |
| PATHIR_Childsub | double |  |  | NO | Childsub |
| PATHIR_PathwayRole_DR | varchar |  | FK | SI | Multidisciplinary Team Role |
| PATHIR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*