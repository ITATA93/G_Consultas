# SQLUser.PA_PersonPatientFlag

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FLAG_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| FLAG_BloodProducts | varchar |  |  | SI | Blood product group, used for massive transfusion ... |
| FLAG_Childsub | double |  |  | NO | Childsub |
| FLAG_CreateUser_DR | bigint |  | FK | SI | The user that adds the patient flag |
| FLAG_DateFrom | date |  |  | SI | Date From |
| FLAG_DateTo | date |  |  | SI | Date To |
| FLAG_LastUpdateUser_DR | bigint |  | FK | SI | The last User that updates the patient flag |
| FLAG_PatientFlag_DR | bigint |  | FK | NO | Des Ref Additional Blood Group |
| FLAG_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*