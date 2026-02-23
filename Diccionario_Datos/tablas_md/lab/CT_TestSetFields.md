# lab.CT_TestSetFields

**Schema:** lab
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSF_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSF_CL_NormalRanges | varchar |  |  | SI | CL Ranges |
| CTTSF_CL_Prompt | double |  |  | SI | CL Prompt |
| CTTSF_CL_Text | varchar |  |  | SI | CL Text |
| CTTSF_CL_Units | varchar |  |  | SI | CL Units |
| CTTSF_CommentHeading | varchar |  |  | SI | Comment Heading |
| CTTSF_DataItem_DR | varchar |  | FK | SI | Data Item |
| CTTSF_DefaultValue | varchar |  |  | SI | Default value |
| CTTSF_EntryFromPE | varchar |  |  | SI | Entry from PE |
| CTTSF_EntryType | varchar |  |  | SI | Entry Type |
| CTTSF_LabelFormat | varchar |  |  | SI | Label Format |
| CTTSF_LabelText | varchar |  |  | SI | Label Text |
| CTTSF_LayoutOrder | varchar |  |  | NO | Layout Order |
| CTTSF_LineNumber | double |  |  | SI | Line Number |
| CTTSF_Order_1 | double |  |  | NO | Field No in Normal layout |
| CTTSF_Order_2 | numeric |  |  | SI | Field No in Cummulative layout |
| CTTSF_Reportable | varchar |  |  | SI | Reportable |
| CTTSF_RowId | varchar |  |  | NO | - |
| CTTSF_TabingOrder | numeric |  |  | SI | Tabing Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*