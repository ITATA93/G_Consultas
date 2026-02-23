# lab.MIF_MachineTestGroup

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MITG_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MITG_Code | varchar |  |  | NO | Code |
| MITG_Desc | varchar |  |  | SI | Description |
| MITG_MaxLoadList | double |  |  | SI | Max Number of patients on loadlist |
| MITG_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*