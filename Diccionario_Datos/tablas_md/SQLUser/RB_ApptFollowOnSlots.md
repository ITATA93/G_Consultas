# SQLUser.RB_ApptFollowOnSlots

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBFOS_ParRef | varchar | PK |  | NO | RB_Appointment Parent Reference |
| RBFOS_ApptSch_DR | varchar |  | FK | SI | Des Ref to ApptSch |
| RBFOS_Childsub | double |  |  | NO | Childsub |
| RBFOS_NoOfSlots | double |  |  | SI | No Of Slots taken up in RBAS by this APPT |
| RBFOS_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*