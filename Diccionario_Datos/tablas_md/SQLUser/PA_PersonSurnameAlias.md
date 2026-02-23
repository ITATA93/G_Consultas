# SQLUser.PA_PersonSurnameAlias

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUR_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| SUR_Active | varchar |  |  | SI | Active |
| SUR_Childsub | double |  |  | NO | Childsub |
| SUR_DNRealOtherName | varchar |  |  | SI | DNRealOtherName |
| SUR_Date | date |  |  | SI | Date |
| SUR_Dob | date |  |  | SI | Dob |
| SUR_FullAliasName | varchar |  |  | SI | FullAliasName |
| SUR_HL7FullAliasText | varchar |  |  | SI | HL7FullAliasText |
| SUR_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| SUR_Name | varchar |  |  | SI | Name |
| SUR_Name2 | varchar |  |  | SI | Name2 |
| SUR_Name3 | varchar |  |  | SI | Name3 |
| SUR_PatientFrom_ID | varchar |  |  | SI | Patient From ID |
| SUR_RowId | varchar |  |  | NO | - |
| SUR_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| SUR_Time | time |  |  | SI | Time |
| SUR_Type | varchar |  |  | SI | Type |
| SUR_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*