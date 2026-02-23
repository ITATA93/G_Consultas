# SQLUser.PA_PersonSchedule

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCH_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| SCH_Childsub | double |  |  | NO | Childsub |
| SCH_Date | date |  |  | SI | Date |
| SCH_RowId | varchar |  |  | NO | - |
| SCH_Schema_DR | bigint |  | FK | SI | Des Ref Schema |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*