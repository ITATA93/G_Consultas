# SQLUser.SS_GroupConsumReason

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONR_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| CONR_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| CONR_Childsub | double |  |  | NO |  Childsub |
| CONR_Reason_DR | bigint |  | FK | SI | Des Ref Reason |
| CONR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*