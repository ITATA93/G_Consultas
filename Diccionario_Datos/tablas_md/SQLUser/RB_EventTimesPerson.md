# SQLUser.RB_EventTimesPerson

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PER_ParRef | varchar | PK |  | NO | RB_EventTimes Parent Reference |
| PER_Childsub | double |  |  | NO | Childsub |
| PER_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| PER_PAPerson_DR | bigint |  | FK | SI | Des Ref PAPerson |
| PER_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*