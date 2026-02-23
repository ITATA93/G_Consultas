# SQLUser.MRC_ICDCodChapterBlockCateg

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CATEG_ParRef | varchar | PK |  | NO | MRC_ICDCodChapterBlock Parent Reference |
| CATEG_Childsub | double |  |  | NO | Childsub |
| CATEG_Code | varchar |  |  | NO | Code |
| CATEG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CATEG_CreatedDate | date |  |  | SI | Created Date |
| CATEG_CreatedTime | time |  |  | SI | Created Time |
| CATEG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CATEG_DateFrom | date |  |  | SI | Date From |
| CATEG_DateTo | date |  |  | SI | Date To |
| CATEG_Desc | varchar |  |  | NO | Description |
| CATEG_RowId | varchar |  |  | NO | - |
| CATEG_UpdatedDate | date |  |  | SI | Updated Date |
| CATEG_UpdatedTime | time |  |  | SI | Updated Time |
| CATEG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q03Q11 | - |  |  | SI | Especialidades Odontológicas |
| Q03Q2 | - |  |  | SI | Tipo de Consulta |
| Q03Q3 | - |  |  | SI | Teleconsulta Hombres Menores de 15 años |
| Q03Q4 | - |  |  | SI | Teleconsulta Mujeres Menores de 15 años |
| Q03Q5 | - |  |  | SI | Teleconsulta Hombres 15 años y más |
| Q03Q6 | - |  |  | SI | Teleconsulta Mujeres 15 años y más |
| Q03Q7 | - |  |  | SI | Modalidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*