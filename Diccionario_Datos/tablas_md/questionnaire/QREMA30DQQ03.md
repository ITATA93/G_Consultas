# questionnaire.QREMA30DQQ03

> Teleconsultas Ambulatorias en Especialidad Odontológica : Teleconsulta Ambulatoria

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Teleconsultas Ambulatorias en Especialidad Odontológica : Teleconsulta Ambulatoria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q11 | varchar |  |  | SI | Especialidades Odontológicas |
| Q03Q2 | varchar |  |  | SI | Tipo de Consulta |
| Q03Q3 | numeric |  |  | SI | Teleconsulta Hombres Menores de 15 años |
| Q03Q4 | numeric |  |  | SI | Teleconsulta Mujeres Menores de 15 años |
| Q03Q5 | numeric |  |  | SI | Teleconsulta Hombres 15 años y más |
| Q03Q6 | numeric |  |  | SI | Teleconsulta Mujeres 15 años y más |
| Q03Q7 | varchar |  |  | SI | Modalidad |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*