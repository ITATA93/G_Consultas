# SQLUser.PA_ExternalDocument

**Schema:** SQLUser
**Columnas:** 48
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXTDOC_RowId | bigint | PK |  | NO | - |
| EXTDOC_Author | varchar |  |  | SI | Author |
| EXTDOC_CreatedDate | date |  |  | SI | Created Date |
| EXTDOC_CreatedTime | time |  |  | SI | Created Time |
| EXTDOC_Date1 | date |  |  | SI | Date1 |
| EXTDOC_Date2 | date |  |  | SI | Date2 |
| EXTDOC_Date3 | date |  |  | SI | Date3 |
| EXTDOC_Date4 | date |  |  | SI | Date4 |
| EXTDOC_Date5 | date |  |  | SI | Date5 |
| EXTDOC_DocType_DR | bigint |  | FK | SI | Des Ref PACExternalDocumentType |
| EXTDOC_ExternalID | varchar |  |  | SI | External ID |
| EXTDOC_HomeCommunityID | varchar |  |  | SI | Home Community ID |
| EXTDOC_HomeRepositoryID | varchar |  |  | SI | Repository ID |
| EXTDOC_Number1 | double |  |  | SI | Number1 |
| EXTDOC_Number2 | double |  |  | SI | Number2 |
| EXTDOC_Number3 | double |  |  | SI | Number3 |
| EXTDOC_Number4 | double |  |  | SI | Number4 |
| EXTDOC_Number5 | double |  |  | SI | Number5 |
| EXTDOC_PAPMI_DR | bigint |  | FK | NO | Des Ref PAPatMas |
| EXTDOC_ROOTCDA_DR | bigint |  | FK | SI | CDA_ROOT document - Des Ref websys.Document |
| EXTDOC_RetrieveDate | date |  |  | SI | Date of document retrieveal |
| EXTDOC_RetrieveTime | time |  |  | SI | Time of document retrieveal |
| EXTDOC_SearchingDate | date |  |  | SI | Searching Date |
| EXTDOC_SearchingTime | time |  |  | SI | Searching Time |
| EXTDOC_Text1 | varchar |  |  | SI | Text1 |
| EXTDOC_Text10 | varchar |  |  | SI | Text10 |
| EXTDOC_Text11 | varchar |  |  | SI | Text11 |
| EXTDOC_Text12 | varchar |  |  | SI | Text12 |
| EXTDOC_Text13 | varchar |  |  | SI | Text13 |
| EXTDOC_Text14 | varchar |  |  | SI | Text14 |
| EXTDOC_Text15 | varchar |  |  | SI | Text15 |
| EXTDOC_Text2 | varchar |  |  | SI | Text2 |
| EXTDOC_Text3 | varchar |  |  | SI | Text3 |
| EXTDOC_Text4 | varchar |  |  | SI | Text4 |
| EXTDOC_Text5 | varchar |  |  | SI | Text5 |
| EXTDOC_Text6 | varchar |  |  | SI | Text6 |
| EXTDOC_Text7 | varchar |  |  | SI | Text7 |
| EXTDOC_Text8 | varchar |  |  | SI | Text8 |
| EXTDOC_Text9 | varchar |  |  | SI | Text9 |
| EXTDOC_Time1 | time |  |  | SI | Time1 |
| EXTDOC_Time2 | time |  |  | SI | Time2 |
| EXTDOC_Time3 | time |  |  | SI | Time3 |
| EXTDOC_Time4 | time |  |  | SI | Time4 |
| EXTDOC_Time5 | time |  |  | SI | Time5 |
| EXTDOC_Title | varchar |  |  | SI | Title |
| Q09Q1 | - |  |  | SI | ¿Acepta? |
| Q09Q2 | - |  |  | SI | Motivo Rechazo |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*