# lab.BBP_PackHistory

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBPH_ParRef | varchar | PK |  | NO | BBP_PackDetails Parent Reference |
| BBPH_Date | date |  |  | SI | Date |
| BBPH_Function | varchar |  |  | SI | Function |
| BBPH_Group | double |  |  | SI | Group |
| BBPH_Item | varchar |  |  | SI | Item |
| BBPH_Order | double |  |  | NO | Order Number |
| BBPH_RowID | varchar |  |  | NO | - |
| BBPH_Time | time |  |  | SI | Time |
| BBPH_User_DR | varchar |  | FK | SI | User DR |
| BBPH_Value_NEW | varchar |  |  | SI | Value NEW |
| BBPH_Value_OLD | varchar |  |  | SI | Value OLD |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*