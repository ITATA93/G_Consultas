# lab.MIF_MachineTestCodes

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MITC_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MITC_DataItem_DR | varchar |  | FK | NO | Des Ref DataItem |
| MITC_Direction | varchar |  |  | SI | Direction |
| MITC_Divider | double |  |  | SI | Default Value |
| MITC_RowId | varchar |  |  | NO | - |
| MITC_Suffix | varchar |  |  | SI | Suffix |
| MITC_XMachineChannel | varchar |  |  | SI | XMachine Channel |
| MITC_xxx2 | varchar |  |  | SI | AA High |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*