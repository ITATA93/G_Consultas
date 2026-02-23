# SQLUser.MR_Pictures

**Schema:** SQLUser
**Columnas:** 40
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PIC_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| PIC_AccessionNo | varchar |  |  | SI | External Document Accession NO |
| PIC_AnaestOper_DR | varchar |  | FK | SI | Des Ref OR_Anaest_Operation |
| PIC_Childsub | double |  |  | NO | Childsub |
| PIC_DateCreated | date |  |  | SI | Date Created |
| PIC_Desc | varchar |  |  | SI | Description |
| PIC_DocSubType_DR | bigint |  | FK | SI | Des Ref DocSubType |
| PIC_DocType_DR | bigint |  | FK | SI | des ref to PAC_DocumentType |
| PIC_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| PIC_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PIC_ExternalID | varchar |  |  | SI | External Document ID |
| PIC_Inactive | varchar |  |  | SI | Inactive |
| PIC_IsExternal | varchar |  |  | SI | IS External Document |
| PIC_LeftCoord | double |  |  | SI | Left Coord |
| PIC_MRCPict_DR | bigint |  | FK | SI | Des Ref to MRCPict |
| PIC_Origin | varchar |  |  | SI | External Document Origin |
| PIC_Path | varchar |  |  | SI | Path |
| PIC_Questionnaire_ControlID | varchar |  |  | SI | Questionnaire Control ID |
| PIC_Questionnaire_DR | bigint |  | FK | SI | Des Ref Questionniare  |
| PIC_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref Reason For Correction |
| PIC_RowId | varchar |  |  | NO | - |
| PIC_TimeCreated | time |  |  | SI | Time Created |
| PIC_TopCoord | double |  |  | SI | Top Coord |
| PIC_Type | varchar |  |  | SI | Type |
| PIC_UpdateDate | date |  |  | SI | UpdateDate |
| PIC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| PIC_UpdateTime | time |  |  | SI | UpdateTime |
| PIC_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| PIC_UserCreated | bigint |  |  | SI | User Created |
| PIC_Visible | varchar |  |  | SI | Visible |
| PIC_WaitList_DR | bigint |  | FK | SI | Des Ref PAWaitingList |
| PIC_websysDocument | bigint |  |  | SI | websysDocument |
| Q55Q1 | - |  |  | SI | IV Check |
| Q55Q2 | - |  |  | SI | IV Access Heparin locked and labeled |
| Q55Q3 | - |  |  | SI | Flush bag pressure checked |
| Q55Q4 | - |  |  | SI | Date |
| Q55Q5 | - |  |  | SI | Time |
| Q55Q6 | - |  |  | SI | Note |
| Q55Q7 | - |  |  | SI | Actions |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*