# questionnaire.QCLXXNRAMQQ57

> Notificación de Sospecha de Reacción Adversa a Medicamentos : Tabla Fármaco Otros

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Notificación de Sospecha de Reacción Adversa a Medicamentos : Tabla Fármaco Otros

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q57Q1 | varchar |  |  | SI | Otro prinicipio activo |
| Q57Q2 | varchar |  |  | SI | Unidad de medida |
| Q57Q3 | date |  |  | SI | Fecha de Vencimiento |
| Q57Q4 | varchar |  |  | SI | Sospecha de excipiente |
| Q57Q5 | varchar |  |  | SI | Nombre de excipiente |
| Q57Q6 | varchar |  |  | SI | Via Administración |
| Q57Q7 | varchar |  |  | SI | Dosis |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*