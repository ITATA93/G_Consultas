# lab.SS_User_SpecialtyAccess

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUCD_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SUCD_PreviousResults | varchar |  |  | SI | Previous Results |
| SUCD_RowID | varchar |  |  | NO | - |
| SUCD_SpecialtyCode_DR | varchar |  | FK | NO | Specialty Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*