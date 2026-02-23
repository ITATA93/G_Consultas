# lab.RG_ReagentMaterialLotAssociation

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RGMLA_ParRef | varchar | PK |  | NO | RG_ReagentMaterialLot Parent Reference |
| RGMLA_RowID | varchar |  |  | NO | - |
| RGMLA_WMAssociation | varchar |  |  | NO | WM Association |
| RGMLA_WMType | varchar |  |  | NO | WM Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*