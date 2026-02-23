# SQLUser.RB_ResOTSessionDeBrief

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTSDB_ParRef | bigint | PK |  | NO | RB_Resource Parent Reference |
| OTSDB_BriefCPType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| OTSDB_BriefCompleted | varchar |  |  | SI | Brief Completed |
| OTSDB_BriefCompletedDate | date |  |  | SI | Brief Completed Date |
| OTSDB_BriefCompletedTime | time |  |  | SI | Brief Completed Time |
| OTSDB_BriefCompleted_DR | bigint |  | FK | SI |  Brief Completed User |
| OTSDB_BriefDate1 | date |  |  | SI |  Brief Date 1 |
| OTSDB_BriefDate2 | date |  |  | SI |  Brief Date 2 |
| OTSDB_BriefDate3 | date |  |  | SI |  Brief Date 3 |
| OTSDB_BriefDate4 | date |  |  | SI |  Brief Date 4 |
| OTSDB_BriefNotRequired | varchar |  |  | SI | Brief Not Required |
| OTSDB_BriefOperatingStaffRole_DR | bigint |  | FK | SI | Brief Operating Staff Role |
| OTSDB_BriefText1 | varchar |  |  | SI | Brief Text 1 |
| OTSDB_BriefText10 | varchar |  |  | SI | Brief Text 10 |
| OTSDB_BriefText11 | varchar |  |  | SI | Brief Text 11 |
| OTSDB_BriefText12 | varchar |  |  | SI | Brief Text 12 |
| OTSDB_BriefText13 | varchar |  |  | SI | Brief Text 13 |
| OTSDB_BriefText14 | varchar |  |  | SI | Brief Text 14 |
| OTSDB_BriefText15 | varchar |  |  | SI | Brief Text 15 |
| OTSDB_BriefText2 | varchar |  |  | SI | Brief Text 2 |
| OTSDB_BriefText3 | varchar |  |  | SI | Brief Text 3 |
| OTSDB_BriefText4 | varchar |  |  | SI | Brief Text 4 |
| OTSDB_BriefText5 | varchar |  |  | SI | Brief Text 5 |
| OTSDB_BriefText6 | varchar |  |  | SI | Brief Text 6 |
| OTSDB_BriefText7 | varchar |  |  | SI | Brief Text 7 |
| OTSDB_BriefText8 | varchar |  |  | SI | Brief Text 8 |
| OTSDB_BriefText9 | varchar |  |  | SI | Brief Text 9 |
| OTSDB_BriefTime1 | time |  |  | SI |  Brief Time 1 |
| OTSDB_BriefTime2 | time |  |  | SI |  Brief Time 2 |
| OTSDB_BriefTime3 | time |  |  | SI |  Brief Time 3 |
| OTSDB_BriefTime4 | time |  |  | SI |  Brief Time 4 |
| OTSDB_BriefYesNo1 | varchar |  |  | SI | Brief YesNo1 |
| OTSDB_BriefYesNo10 | varchar |  |  | SI | Brief YesNo10 |
| OTSDB_BriefYesNo11 | varchar |  |  | SI | Brief YesNo11 |
| OTSDB_BriefYesNo12 | varchar |  |  | SI | Brief YesNo12 |
| OTSDB_BriefYesNo13 | varchar |  |  | SI | Brief YesNo13 |
| OTSDB_BriefYesNo14 | varchar |  |  | SI | Brief YesNo14 |
| OTSDB_BriefYesNo15 | varchar |  |  | SI | Brief YesNo15 |
| OTSDB_BriefYesNo2 | varchar |  |  | SI | Brief YesNo2 |
| OTSDB_BriefYesNo3 | varchar |  |  | SI | Brief YesNo3 |
| OTSDB_BriefYesNo4 | varchar |  |  | SI | Brief YesNo4 |
| OTSDB_BriefYesNo5 | varchar |  |  | SI | Brief YesNo5 |
| OTSDB_BriefYesNo6 | varchar |  |  | SI | Brief YesNo6 |
| OTSDB_BriefYesNo7 | varchar |  |  | SI | Brief YesNo7 |
| OTSDB_BriefYesNo8 | varchar |  |  | SI | Brief YesNo8 |
| OTSDB_BriefYesNo9 | varchar |  |  | SI | Brief YesNo9 |
| OTSDB_Childsub | double |  |  | NO | Childsub |
| OTSDB_CreateDate | date |  |  | SI |  Date Created |
| OTSDB_CreateTime | time |  |  | SI |  Time Created |
| OTSDB_CreateUser_DR | bigint |  | FK | SI |   User Created |
| OTSDB_Date | date |  |  | SI | Date |
| OTSDB_DeBriefCPType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| OTSDB_DeBriefCompleted | varchar |  |  | SI | DeBrief Completed |
| OTSDB_DeBriefCompletedDate | date |  |  | SI | DeBrief Completed Date |
| OTSDB_DeBriefCompletedTime | time |  |  | SI | DeBrief Completed Time |
| OTSDB_DeBriefCompleted_DR | bigint |  | FK | SI |  DeBrief Completed User |
| OTSDB_DeBriefDate1 | date |  |  | SI |  DeBrief Date 1 |
| OTSDB_DeBriefDate2 | date |  |  | SI |  DeBrief Date 2 |
| OTSDB_DeBriefDate3 | date |  |  | SI |  DeBrief Date 3 |
| OTSDB_DeBriefDate4 | date |  |  | SI |  DeBrief Date 4 |
| OTSDB_DeBriefOperatingStaffRole_DR | bigint |  | FK | SI | Debrief Operating Staff Role |
| OTSDB_DeBriefText1 | varchar |  |  | SI | DeBrief Text 1 |
| OTSDB_DeBriefText10 | varchar |  |  | SI | DeBrief Text 10 |
| OTSDB_DeBriefText2 | varchar |  |  | SI | DeBrief Text 2 |
| OTSDB_DeBriefText3 | varchar |  |  | SI | DeBrief Text 3 |
| OTSDB_DeBriefText4 | varchar |  |  | SI | DeBrief Text 4 |
| OTSDB_DeBriefText5 | varchar |  |  | SI | DeBrief Text 5 |
| OTSDB_DeBriefText6 | varchar |  |  | SI | DeBrief Text 6 |
| OTSDB_DeBriefText7 | varchar |  |  | SI | DeBrief Text 7 |
| OTSDB_DeBriefText8 | varchar |  |  | SI | DeBrief Text 8 |
| OTSDB_DeBriefText9 | varchar |  |  | SI | DeBrief Text 9 |
| OTSDB_DeBriefTime1 | time |  |  | SI |  DeBrief Time 1 |
| OTSDB_DeBriefTime2 | time |  |  | SI |  DeBrief Time 2 |
| OTSDB_DeBriefTime3 | time |  |  | SI |  DeBrief Time 3 |
| OTSDB_DeBriefTime4 | time |  |  | SI |  DeBrief Time 4 |
| OTSDB_DeBriefYesNo1 | varchar |  |  | SI | DeBrief YesNo1 |
| OTSDB_DeBriefYesNo10 | varchar |  |  | SI | DeBrief YesNo10 |
| OTSDB_DeBriefYesNo2 | varchar |  |  | SI | DeBrief YesNo2 |
| OTSDB_DeBriefYesNo3 | varchar |  |  | SI | DeBrief YesNo3 |
| OTSDB_DeBriefYesNo4 | varchar |  |  | SI | DeBrief YesNo4 |
| OTSDB_DeBriefYesNo5 | varchar |  |  | SI | DeBrief YesNo5 |
| OTSDB_DeBriefYesNo6 | varchar |  |  | SI | DeBrief YesNo6 |
| OTSDB_DeBriefYesNo7 | varchar |  |  | SI | DeBrief YesNo7 |
| OTSDB_DeBriefYesNo8 | varchar |  |  | SI | DeBrief YesNo8 |
| OTSDB_DeBriefYesNo9 | varchar |  |  | SI | DeBrief YesNo9 |
| OTSDB_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| OTSDB_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| OTSDB_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| OTSDB_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| OTSDB_NotesHTMLPlainText1 | bigint |  |  | SI | Brief Notes  Plain Text Des Ref websys.Document |
| OTSDB_NotesHTMLPlainText2 | bigint |  |  | SI | DeBrief Notes  Plain Text Des Ref websys.Document |
| OTSDB_NotesHTMLPlainText3 | bigint |  |  | SI | Brief Notes  Plain Text 2 Des Ref websys.Document |
| OTSDB_NotesHTMLPlainText4 | bigint |  |  | SI | DeBrief Notes  Plain Text 2 Des Ref websys.Documen... |
| OTSDB_NotesHTMLRichText1 | bigint |  |  | SI | Brief Notes Rich Text Des Ref websys.Document |
| OTSDB_NotesHTMLRichText2 | bigint |  |  | SI | DeBrief Notes Rich Text Des Ref websys.Document |
| OTSDB_NotesHTMLRichText3 | bigint |  |  | SI | Brief Notes Rich Text 2 Des Ref websys.Document |
| OTSDB_NotesHTMLRichText4 | bigint |  |  | SI | DeBrief Notes Rich Text 2 Des Ref websys.Document |
| OTSDB_RBApptSchedule_DR | varchar |  | FK | SI | Des Ref RBApptSchedule |
| OTSDB_RBEffDateSession_DR | varchar |  | FK | SI | Des Ref RBEffDateSession |
| OTSDB_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*