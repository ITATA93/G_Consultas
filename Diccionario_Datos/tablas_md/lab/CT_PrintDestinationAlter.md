# lab.CT_PrintDestinationAlter

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPDA_ParRef | varchar | PK |  | NO | CT_PrintDestination Parent Reference |
| CTPDA_Destination_DR | varchar |  | FK | SI | Destination DR |
| CTPDA_Order | double |  |  | NO | Order |
| CTPDA_RowID | varchar |  |  | NO | - |
| CTPDA_TimeEnd | time |  |  | SI | Time End |
| CTPDA_TimeStart | time |  |  | SI | Time Start |
| CTPDA_WeekDay | varchar |  |  | SI | Week Day |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*