# SQLUser.PA_PersonAlias

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALIAS_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ALIAS_Active | varchar |  |  | SI | Active |
| ALIAS_Childsub | double |  |  | NO | Childsub |
| ALIAS_DNRealOtherName | varchar |  |  | SI | SURDNRealOtherName |
| ALIAS_DOB | date |  |  | SI | DOB |
| ALIAS_Date | date |  |  | SI | Date |
| ALIAS_FullAliasName | varchar |  |  | SI | FullAliasName |
| ALIAS_GivenName | varchar |  |  | SI | Given Name |
| ALIAS_HL7FullAliasText | varchar |  |  | SI | HL7FullAliasText |
| ALIAS_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| ALIAS_NameID | varchar |  |  | SI | Name ID |
| ALIAS_NameSource_DR | bigint |  | FK | SI | Name Source |
| ALIAS_NameType_DR | bigint |  | FK | SI | Name Type |
| ALIAS_OtherName | varchar |  |  | SI | Other Name |
| ALIAS_PatientFrom_ID | varchar |  |  | SI | Patient From |
| ALIAS_PreferredName | varchar |  |  | SI | Preferred Name |
| ALIAS_RowId | varchar |  |  | NO | - |
| ALIAS_Sex_DR | bigint |  | FK | SI | Sex |
| ALIAS_Surname | varchar |  |  | SI | Surname |
| ALIAS_Text | varchar |  |  | SI | Text |
| ALIAS_Time | time |  |  | SI | Time |
| ALIAS_Title_DR | bigint |  | FK | SI | Title |
| ALIAS_Type | varchar |  |  | SI | Type |
| ALIAS_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*