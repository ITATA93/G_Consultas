# SQLUser.OE_OrderItemChangeDosing

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOSE_ParRef | bigint | PK |  | NO | OE_OrderItemChange Parent Reference |
| ChildQ34DR | - |  |  | SI | Child Reference: Knee |
| DOSE_Action | varchar |  |  | SI | Action  |
| DOSE_Childsub | double |  |  | NO | Childsub |
| DOSE_NewDate | date |  |  | SI | New Date |
| DOSE_NewDose | double |  |  | SI | NewDose |
| DOSE_NewInstruction | varchar |  |  | SI | DOSENewInstruction   |
| DOSE_NewIsConditional | varchar |  |  | SI | Modified OEOREIsConditional |
| DOSE_NewOffsetExec_DR | varchar |  | FK | SI | New Offset Exec DR |
| DOSE_NewOffsetItem_DR | varchar |  | FK | SI | New Offset Item DR |
| DOSE_NewOffsetType | varchar |  |  | SI | New Offset Type |
| DOSE_NewOffsetUnit | varchar |  |  | SI | New Offset Unit |
| DOSE_NewOffsetValue | double |  |  | SI | New Offset Value  |
| DOSE_NewTime | time |  |  | SI | NewTime |
| DOSE_NewUom_DR | bigint |  | FK | SI | Des Ref CTUOM |
| DOSE_OrdExec_DR | varchar |  | FK | SI | Des Ref OEOrdExec  |
| DOSE_OriginalDate | date |  |  | SI | Original Date |
| DOSE_OriginalDose | double |  |  | SI | OriginalDose |
| DOSE_OriginalInstruction | varchar |  |  | SI | OriginalInstruction   |
| DOSE_OriginalIsConditional | varchar |  |  | SI | Original OEOREIsConditional |
| DOSE_OriginalOffsetExec_DR | varchar |  | FK | SI | Original Offset Exec DR |
| DOSE_OriginalOffsetItem_DR | varchar |  | FK | SI | Original Offset Item DR |
| DOSE_OriginalOffsetType | varchar |  |  | SI | Original Offset Type |
| DOSE_OriginalOffsetUnit | varchar |  |  | SI | Original Offset Unit |
| DOSE_OriginalOffsetValue | double |  |  | SI | Original Offset Value  |
| DOSE_OriginalTime | time |  |  | SI | OriginalTime |
| DOSE_OriginalUom_DR | bigint |  | FK | SI | Des Ref CTUOM |
| DOSE_RowId | varchar |  |  | NO | - |
| DOSE_UpdatedDate | date |  |  | SI | Updated Date |
| DOSE_UpdatedTime | time |  |  | SI | UpdatedTime |
| DOSE_UpdatedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q33Q1 | - |  |  | SI | Movement |
| Q33Q2 | - |  |  | SI | Strength - Right |
| Q33Q3 | - |  |  | SI | Strength - Left |
| Q33Q4 | - |  |  | SI | AROM - Right |
| Q33Q5 | - |  |  | SI | AROM - Left |
| Q33Q6 | - |  |  | SI | PROM - Right |
| Q33Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*