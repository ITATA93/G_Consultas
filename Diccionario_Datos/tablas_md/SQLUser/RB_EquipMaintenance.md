# SQLUser.RB_EquipMaintenance

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBEM_RowId | bigint | PK |  | NO | - |
| RBEM_EquipmentList_DR | varchar |  | FK | SI | Des Ref EquipmentList |
| RBEM_Equipment_DR | bigint |  | FK | SI | Des Ref Equipment |
| RBEM_ReasonNA_DR | bigint |  | FK | SI | Des Ref ReasonNA |
| RBEM_SerialNo | varchar |  |  | SI | Not Used |
| RBEM_UnavDateFrom | date |  |  | SI | UnavDateFrom |
| RBEM_UnavDateTo | date |  |  | SI | UnavDateTo |
| RBEM_UnavTimeFrom | time |  |  | SI | UnavTimeFrom |
| RBEM_UnavTimeTo | time |  |  | SI | UnavTimeTo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*