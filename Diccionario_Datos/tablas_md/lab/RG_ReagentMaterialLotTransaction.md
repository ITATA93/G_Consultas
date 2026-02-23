# lab.RG_ReagentMaterialLotTransaction

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RGMLT_ParRef | varchar | PK |  | NO | RG_ReagentMaterialLot Parent Reference |
| RGMLT_Date | date |  |  | SI | Date |
| RGMLT_RowID | varchar |  |  | NO | - |
| RGMLT_Sequence | double |  |  | NO | Sequence |
| RGMLT_Time | time |  |  | SI | Time |
| RGMLT_TransactionType | varchar |  |  | SI | Transaction Type |
| RGMLT_Units | double |  |  | SI | Units |
| RGMLT_User_DR | varchar |  | FK | SI | User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*