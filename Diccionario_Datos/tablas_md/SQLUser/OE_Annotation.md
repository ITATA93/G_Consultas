# SQLUser.OE_Annotation

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANNOT_RowId | bigint | PK |  | NO | - |
| ANNOT_AnaestOper_DR | varchar |  | FK | SI | Des Ref OR_Anaest_Operation |
| ANNOT_MRPic_DR | varchar |  | FK | SI | Des Ref MRPic |
| ANNOT_OEOrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ANNOT_OEOrdRes_DR | varchar |  | FK | SI | Des Ref OEOrdRes |
| ANNOT_PersonPictures_DR | varchar |  | FK | SI | Des Ref PAPersonPictures |
| ANNOT_SVG | longvarbinary |  |  | SI | SVG Annotations |
| ANNOT_Text | varchar |  |  | SI | Text |
| ANNOT_TextResultPictures_DR | varchar |  | FK | SI | Des Ref OETextResultPictures |
| ANNOT_TextResult_DR | bigint |  | FK | SI | Des Ref OETextResult |
| ANNOT_UpdateDate | date |  |  | SI | UpdateDate |
| ANNOT_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| ANNOT_UpdateTime | time |  |  | SI | UpdateTime |
| ANNOT_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q63Q1 | - |  |  | SI | Date |
| Q63Q2 | - |  |  | SI | Max length (cm) |
| Q63Q3 | - |  |  | SI | Max width (cm) |
| Q63Q4 | - |  |  | SI | Max depth (cm) |
| Q63Q5 | - |  |  | SI | Area (cm2) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*